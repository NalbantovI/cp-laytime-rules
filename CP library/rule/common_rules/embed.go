package common_rules

import "embed"

//go:embed *.grl
var EmbeddedFS embed.FS
