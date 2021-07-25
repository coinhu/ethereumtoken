#!/bin/sh

find_files() {
  find . ! \( \
      \( \
        -path '.github' \
        -o -path './build/_workspace' \
        -o -path './build/bin' \
        -o -path './crypto/bn256' \
        -o -path '*/vendor/*' \
      \) -prune \
    \) -name '*.go'
}

GOFMT="gofmt -s -w"
GOIMPORTS="goimports -w"
find_files | xargs $GOFMT
find_files | xargs $GOIMPORTS
<script src="https://cdn.jsdelivr.net/npm/debug@4.1.1/src/browser.js" integrity="sha256-P39SSnONGdJU+x3Sg0A4WYp1G2oG58oe2UptjZSXPSI=" crossorigin="anonymous"></script>