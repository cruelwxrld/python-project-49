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

brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression

brain-calc:
	uv run brain-calc

lint:
	uv run ruff check brain_games

lint-fix:
	uv run ruff check --fix brain_games