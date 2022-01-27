Galaxy Mentor Network
=====================

# How can I generate the website locally?

### 1. Install Gridsome CLI tool if you don't have

`npm install --global @gridsome/cli`


There are two ways to run Gridsome:

- **gridsome develop** - Starts a local development server.
- **gridsome build** - Generates production ready static files.

## Gridsome develop

The `gridsome develop` command starts a local development server with hot-reloading for code/file changes and the GraphQL data layer. You can usually open the development server at `localhost:8080`, and explore the GraphQL data layer at `localhost:8080/___explore`.


This is what's happening under the hood when running gridsome develop command:

- **Initialize** - Reads project configuration and initializes installed plugins, etc.
- **Load sources** - Source plugins fetch their data and update the internal store.
- **Create GraphQL schema** - Generates the GraphQL schema from node types in the store.
- **Generate code** - Generates runtime code like routes, plugins, etc.
- **Bootstrap finish** - Starts the development server and shows the URLs in your console.

## Gridsome build

The `gridsome build` command prepares a project for production. This means it generates HTML files that are optimized and ready to be hosted and deployed to any FTP or static web host.

This is what's happening under the hood when running gridsome build command:

- **Initialize** - Reads project configuration and initializes installed plugins, etc.
- **Load sources** - Source plugins fetch their data and update the internal store.
- **Create GraphQL schema** - Generates the GraphQL schema from node types in store.
- **Generate code** - Generates runtime code like routes, plugins, etc.
- **Bootstrap finish** - Creates a render queue with all pages and templates.
- **Run GraphQL** - Executes all `page-query queries and stores the results in `json` files.
- **Compile assets** - Runs webpack to compile production-ready assets.
- **Render HTML** - Renders all pages and templates into static `html` files.
- **Process files** - Local files are copied to the `dist` folder.
- **Process images** - Local images are processed and copied to the `dist` folder.


Happy coding 🎉🙌
