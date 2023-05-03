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

**Note**: the above command can fail with Node.js v17.0.0 with the error:

```
...
  opensslErrorStack: [ 'error:03000086:digital envelope routines::initialization error' ],
  library: 'digital envelope routines',
  reason: 'unsupported',
  code: 'ERR_OSSL_EVP_UNSUPPORTED'
}

Node.js v17.0.0
```

As stated in [this issue](https://github.com/vercel/next.js/issues/30078#issuecomment-947338268), it can be solved with:

```sh
$ export NODE_OPTIONS=--openssl-legacy-provider
```

## Creating a static page written in Markdown

1. Create a markdown file in `content` folder


    To add an image:
    1. Add the image to the `content/images` folder
    2. Import it in the Markdown with `![Alternative text](./images/<filename>)` ([Gridsome documentation](https://gridsome.org/docs/images/#usage-in-markdown))

2. Copy on the top of the file the following:

    ```
    ---
    id: <id>
    title: <Title>
    ---
    ```

3. Replace
    - `<id>` by the filename
    - `<Title>` by a title for the page
4. Create a `<Id>.vue` (replace `<Id>` by the previous filename) file in `src/pages/`
5. Copy on the top of the file the following:

    ```
    <template>
        <Layout>
            <h1 class="page-title">{{ $page.main.title }}</h1>
            <div class="markdown" v-html="$page.main.content" />
        </Layout>
    </template>

    <page-query>
    query {
        main: insert (path: "/content/<id>/") {
            id
            title
            content
            fileInfo {
                path
            }
        }
    }
    </page-query>

    <script>
    export default {
        metaInfo: {
            title: "GMN - <Short title>"
        }
    }
    </script>
    ```

6. Replace
    - `<id>` by the filename
    - `<Short title>` by a short title for the page

## Creating a static page in Vue

1. Create a `<Name>.vue` file in `src/pages/`
2. Fill your file following the structure below:

    ```
    <template>
        <Layout>

            <h1>Title</h1>

            <!-- Add content using HTML and Bootstrap-Vue components (except the ones including images)

            Bootstrap-Vue doc: https://bootstrap-vue.org/docs/components/

            ---!>

        </Layout>
    </template>

    <script>
    export default {
    metaInfo: {
        title: 'Galaxy Mentoring Network'
    }
    }
    </script>
    ```

3. To add an image:
    1. Add the images to `src/images` folder
    2. Import it in the Vue file using `<g-image src="~/images/<filename>" alt="Alternative text"/> ([Gridsome documentation](https://gridsome.org/docs/images/))


## Format mentee applications

1. Install Python and pandas
2. Put the link to application sheet in `bin/get_applications.sh`
2. Run `bash bin/get_applications.sh`