import asyncio
from quart import Quart, render_template, url_for


app = Quart(__name__)


@app.get("/")
async def index():
    return await render_template("index.html")


@app.get("/poll")
async def poll():
    return await render_template("index.html", endpoints=await site_map())


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.get("/site-map")
async def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint in EXCLUDED_ENDPOINTS:
            continue
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    return links


def main():
    app.run()


if __name__ == "__main__":
    EXCLUDED_ENDPOINTS = [site_map.__name__]
    main()
