FROM node:18-alpine

WORKDIR /app

# Install deps
COPY package.json package-lock.json* ./
# Install dependencies (do not swallow errors so build fails if something is missing)
RUN npm install --no-audit --no-fund

# Copy source and run dev server
COPY . .

# Expose Vite default port
EXPOSE 5173

# Use the dev script so Vite serves with HMR and binds to 0.0.0.0
CMD ["npm", "run", "dev"]
