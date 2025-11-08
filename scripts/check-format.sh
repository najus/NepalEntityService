#!/bin/bash
# Check formatting without modifying files
# Used in CI to verify code is properly formatted

set -e

echo "🔍 Checking code formatting..."

echo ""
echo "🎨 Checking black formatting..."
poetry run black --check .

echo ""
echo "📦 Checking import sorting with isort..."
poetry run isort --check-only .

echo ""
echo "✅ Checking code with flake8..."
poetry run flake8 .

echo ""
echo "✨ All formatting checks passed!"
