package yara

import "embed"

//go:embed *.grl
var EmbeddedFS embed.FS
