# Build Stage
FROM node:22-alpine AS builder

WORKDIR /deckify-web

COPY package.json yarn.lock  ./

RUN yarn install

COPY src ./src
COPY public ./public
COPY next.config.ts postcss.config.mjs tsconfig.json ./

RUN yarn build

# Runtime Stage
FROM node:22-alpine AS runtime

WORKDIR /deckify-web

COPY --from=builder /deckify-web/.next ./.next
COPY --from=builder /deckify-web/public ./public
COPY --from=builder /deckify-web/node_modules ./node_modules
COPY --from=builder /deckify-web/package.json ./

EXPOSE 3000

CMD ["yarn", "start"]