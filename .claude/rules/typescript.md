---
paths:
  - "frontend/**/*.ts"
  - "frontend/**/*.tsx"
---

# TypeScript Rules

## Code Style

- Indent: 2 spaces
- Line width: 88
- Semicolons: always
- String quotes: double quotes
- Trailing commas: ES5 style (objects, arrays, function params)
- Arrow function parentheses: always — `(x) => x` not `x => x`
- Use template literals instead of string concatenation (enforced by Biome `style.useTemplate`)
- Imports are auto-organized by Biome `assist.organizeImports`
- Run `yarn format` (biome check --write) before committing

## Type Annotations

- TypeScript strict mode is enforced (`strict: true` in tsconfig)
- Always annotate function return types explicitly
- Prefer `interface` for object shapes, `type` for unions, intersections, and aliases
- Never use `any`; use `unknown` when the type is truly unknown and narrow it before use
- Avoid type assertions (`as`) unless absolutely necessary; prefer type guards

## Naming Conventions

- Variables and functions: `camelCase`
- Types, interfaces, enums, and classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE` only for module-level primitive constants
- Boolean variables: prefix with `is`, `has`, `can`, or `should`

## General Best Practices

- Prefer `const` over `let`; never use `var`
- Use optional chaining (`?.`) and nullish coalescing (`??`) over manual null checks
- Avoid non-null assertions (`!`); handle nullable values explicitly
- Prefer `===` over `==`
- Avoid deeply nested callbacks; use `async/await` for asynchronous code
- Do not suppress linter errors with inline comments unless there is a documented reason
