FROM nginx:alpine AS base

# Create non-root user
RUN addgroup -g 10001 -S appuser && \
    adduser -u 10001 -S appuser -G appuser

# Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Copy static website files
COPY index.html /usr/share/nginx/html/
COPY styles.css /usr/share/nginx/html/

# Set ownership and create tmp directories
RUN chown -R appuser:appuser /usr/share/nginx/html && \
    chown appuser:appuser /etc/nginx/nginx.conf && \
    chmod 644 /etc/nginx/nginx.conf && \
    mkdir -p /tmp/client_temp /tmp/proxy_temp /tmp/fastcgi_temp /tmp/uwsgi_temp /tmp/scgi_temp && \
    chown -R appuser:appuser /tmp && \
    mkdir -p /var/cache/nginx && \
    chown -R appuser:appuser /var/cache/nginx && \
    mkdir -p /var/log/nginx && \
    chown -R appuser:appuser /var/log/nginx

# Switch to non-root user
USER appuser

# Expose port 3000
EXPOSE 3000

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
