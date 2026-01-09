FROM python:3.12-slim AS build

# Run ldconfig to update library cache
RUN /sbin/ldconfig /usr/local/lib

# Final minimal image
FROM scratch

# Copy Python runtime and required libraries
COPY --from=build /usr/local/lib /usr/local/lib
COPY --from=build /usr/local/bin/python3.12 /usr/bin/python3
COPY --from=build /lib/x86_64-linux-gnu/libc.so.6 /lib/x86_64-linux-gnu/libc.so.6
COPY --from=build /lib/x86_64-linux-gnu/libm.so.6 /lib/x86_64-linux-gnu/libm.so.6
COPY --from=build /lib/x86_64-linux-gnu/libz.so.1 /lib/x86_64-linux-gnu/libz.so.1
COPY --from=build /lib64/ld-linux-x86-64.so.2 /lib64/ld-linux-x86-64.so.2
COPY --from=build /etc/ld.so.cache /etc/ld.so.cache
COPY ./main.py .