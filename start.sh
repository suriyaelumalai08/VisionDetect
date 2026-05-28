#!/usr/bin/env bash
set -e

PORT="${PORT:-10000}"

echo "Starting VisionDetect on 0.0.0.0:${PORT}"
exec gunicorn app:app --bind "0.0.0.0:${PORT}" --workers 1 --timeout 300
