# my-app

## Launch LangServe

```bash
export HUGGINGFACEHUB_API_TOKEN=$HUGGINGFACEHUB_API_TOKEN
```

```bash
langchain serve
```

## Running in Docker

### Building the Image

To build the image, you simply:

```shell
docker build . -t my-langserve-app
```

If you tag your image with something other than `my-langserve-app`,
note it for use in the next step.

### Running the Image Locally

To run the image, you'll need to include any environment variables
necessary for your application.

In the below example, we inject the `HUGGINGFACEHUB_API_TOKEN` environment
variable with the value set in my local environment
(`$HUGGINGFACEHUB_API_TOKEN`)

We also expose port 8080 with the `-p 8080:8080` option.

```shell
docker run -e HUGGINGFACEHUB_API_TOKEN=$HUGGINGFACEHUB_API_TOKEN -p 8080:8080 my-langserve-app
```
