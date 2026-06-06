#!/bin/bash

echo "Warning: create-gihub-comments.sh is deprecated; use create-github-comments.sh instead." >&2
exec "$(dirname "$0")/create-github-comments.sh" "$@"
