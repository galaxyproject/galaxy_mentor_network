<template>
    <Layout>
        <h1 class="page-title">{{ $page.main.title }}</h1>
        <div class="markdown" v-html="$page.main.content" />
    </Layout>
</template>

<page-query>
query {
    main: insert (path: "/content/application/") {
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
        title: "GMN - Application Guidelines"
    }
}
</script>
