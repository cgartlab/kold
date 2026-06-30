# Makefile — Kold

VERSION := $(shell cat VERSION)

.PHONY: help
help:
	@echo "Kold Makefile"
	@echo ""
	@echo "  make check-version   — show current version"
	@echo "  make bump-patch     — bump PATCH (e.g. 0.2.0 → 0.2.1)"
	@echo "  make bump-minor     — bump MINOR (e.g. 0.2.0 → 0.3.0)"
	@echo "  make bump-major     — bump MAJOR (e.g. 0.2.0 → 1.0.0)"
	@echo "  make setup          — install lint dependencies"
	@echo "  make lint           — run HTML/CSS lint checks"
	@echo "  make validate       — run all quality checks (version + lint)"
	@echo "  make release        — commit, tag and push a release"
	@echo "  make package        — create release archive"
	@echo "  make clean          — remove generated files"
	@echo ""
	@echo "  Current version: $(VERSION)"

# ─── Version queries ─────────────────────────────────────────────
.PHONY: check-version
check-version:
	@echo "Current version: $(VERSION)"

# ─── Version bumping ─────────────────────────────────────────────
.PHONY: bump-patch bump-minor bump-major
bump-patch bump-minor bump-major: BUMP_KIND=$(notdir $(firstword $(MAKECMDGOALS)))
bump-patch bump-minor bump-major:
	@python3 tools/bump_version.py $(BUMP_KIND)
	@echo ""
	@echo "Files staged. Review, then: make validate && make release"

# ─── Setup ──────────────────────────────────────────────────────
.PHONY: setup
setup:
	@npm install

# ─── Lint ─────────────────────────────────────────────────────────
.PHONY: lint
lint: setup
	@npm run lint

# ─── Validation ──────────────────────────────────────────────────
.PHONY: validate
validate:
	@echo "Running quality checks..."
	@python3 tools/validate_versioning.py
	@echo ""
	@echo "Running lint..."
	@npm run lint

_check-core-files:
	@echo "Checking core files exist..."
	@for f in AGENTS.md SKILL.md README.md VERSION LICENSE; do \
	  test -f "$$f" && echo "  $$f ok" || (echo "  $$f missing"; exit 1); \
	done

# ─── Release ─────────────────────────────────────────────────────
.PHONY: release
release: validate
	@echo "Checking for staged changes..."
	@git diff --quiet --cached \
	  || { echo "Uncommitted changes found. Commit or stash first."; exit 1; }
	@echo "Creating commit and tag for v$(VERSION)..."
	@git commit -m "chore(release): v$(VERSION)" || { echo "Nothing to commit"; exit 0; }
	@git tag v$(VERSION)
	@echo "Pushing main and tag..."
	@git push origin main && git push origin tags/v$(VERSION)
	@echo ""
	@echo "Released v$(VERSION) — GitHub Actions will create the Release page"

# ─── Package ─────────────────────────────────────────────────────
.PHONY: package
package:
	@mkdir -p dist
	@tar --exclude='.git' --exclude='dist' -czf dist/kold-v$(VERSION).tar.gz .
	@zip -q dist/kold-v$(VERSION).zip . -r -x '.git/*' -x 'dist/*'
	@echo "Packages created: dist/kold-v$(VERSION).tar.gz dist/kold-v$(VERSION).zip"

# ─── Clean ────────────────────────────────────────────────────────
.PHONY: clean
clean:
	@rm -rf dist
	@echo "Cleaned"
