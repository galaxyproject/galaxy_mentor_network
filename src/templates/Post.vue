<template>
    <Layout>
        <article>
            <header>
                <h1>{{ $page.post.title }}</h1>
                <p>Published on {{ $page.post.date }}</p>
            </header>

            <main class="content" v-html="$page.post.content"></main>
        </article>
    </Layout>
</template>

<style>
article > header {
  text-align: center;
}

.content {
  margin-top: 48px;
}
</style>

<page-query>
query Post ($path: String!) {
   post: post (path: $path) {
    id
    title
    date (format: "MMMM D, YYYY")
    summary
    content
  }
}
</page-query>