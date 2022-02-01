<template>
    <div class="post-list">
        <article class="post" v-for="post in posts" :key="post.node.id">
            <h4>{{post.node.title}}</h4>
            <p>Published on {{post.node.date}}</p>
            <g-link :to="post.node.path">Read article</g-link>
        </article>
    </div>
</template>

<script>
export default {
  props: ['posts']
}
</script>

<style>
.post-list {
  margin-top: 12px;
}

.post {
  padding: 12px 0;
}
</style>
