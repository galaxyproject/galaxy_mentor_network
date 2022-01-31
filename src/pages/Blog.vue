<template>
  <Layout>
    <h1>Blog</h1>

    <PostList :posts="$page.posts.edges"/>

  </Layout>
</template>

<page-query>
query {
  posts: allPost {
    edges {
      node {
        id
        title
        date (format: "MMMM D, YYYY")
        path
      }
    }
  }
}
</page-query>

<script>
import PostList from '~/components/PostList.vue';

export default {
  metaInfo: {
    title: 'GMN - Blog'
  },
  components: {
    PostList
  }
}
</script>