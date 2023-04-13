# Use the official Node.js image as the base image for building the React application
FROM node:18.15.0 AS builder

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY vite-react/package*.json ./

# Install the dependencies
RUN yarn install --frozen-lockfile

# Copy the entire React application from the host to the container
COPY vite-react ./

# Build the React application
RUN yarn run build

# Use the official Nginx image as the base image for serving the React application
FROM nginx:1.21.3-alpine

# Copy the built React application from the builder stage to the Nginx container
COPY --from=builder /app/dist /usr/share/nginx/html

# Expose port 80 for incoming HTTP traffic
EXPOSE 80

# Start Nginx and keep it running in the foreground
CMD ["nginx", "-g", "daemon off;"]
