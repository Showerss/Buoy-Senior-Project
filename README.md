# Buoy Project

A Go project following best practices for structure and organization.

## Project Structure

```
.
├── cmd/              # Command-line applications
│   └── main.go       # Main entry point
├── internal/         # Private packages
│   └── pkg/         # Internal packages
├── tests/           # Test files
└── go.mod          # Go module definition
```

## Development Setup

1. Ensure Go is installed (version 1.21 or higher)
2. Run `go mod tidy` to download dependencies
3. Run tests with `go test ./...`

## Adding New Components

Use the scaffold tool to generate new components:

```bash
scaffold generate component <name>
```

## Documentation

- Design documents: [docs/design/](docs/design/)
- UML diagrams: [docs/uml/](docs/uml/)
