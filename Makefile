install: 
	uv sync

package-install:
	uv tool install dist/*.whl

brain-games: 
	uv run brain-games

lint:
	uv run ruff check brain_games

lint-fix:
	uv run ruff check --fix brain_games