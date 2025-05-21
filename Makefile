install: 
	uv sync

build: 
	uv build

package-install:
	uv tool install dist/*.whl

brain-games: 
	uv run brain-games

brain-even:
	uv run brain-even

lint:
	uv run ruff check brain_games

lint-fix:
	uv run ruff check --fix brain_games