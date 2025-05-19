install: 
	uv sync

package-install:
	uv tool install dist/*.whl

brain-games: 
	uv run brain-games