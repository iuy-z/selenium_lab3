FROM python:3.10-slim
WORKDIR /tests
COPY selenium_tests/ .
RUN pip install selenium
RUN apt-get update && apt-get install -y chromium-driver chromium-browser
CMD ["pytest", "."]
