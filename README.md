Galaxy Mentor Network
=====================

# How can I generate the website locally?

## Requirements

- Node.js

## Getting started

You can get the site running locally by first cloning this repo:

```sh
$ git clone https://github.com/bebatut/galaxy_mentor_network.git
```

Then install the dependencies:

```sh
$ cd galaxy_mentor_network
$ npm install
```

Then you can build the site in development mode to run it in a local server (at http://localhost:8080) and see your content:

```sh
$ npm run develop
```

This command includes a hot reloader which will update the site automatically each time you edit a file.
Note: There's a [minor known issue](https://github.com/galaxyproject/galaxy-hub/issues/748) that can occur when you're renaming/moving/deleting directories or image files. If you're finding the development server crashes too often, try adding the arguments `--resource copy` to the `yarn develop` command. This fixes the issue, at the cost of a far larger build directory (because all images are copied to it instead of linked).

To generate the static files for the entire site, just run `build` instead:

```sh
$ nprm run build
```

The static files can then be found in the `dist` directory.

## Creating static pages

