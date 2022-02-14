<template>
     <Layout>
         <b-row>
      <b-col lg="7" md="7">
            <h1 class="page-title">{{ $page.main.title }}</h1>
            <div class="markdown" v-html="$page.main.content" /> 
         </b-col>
      <b-col lg="5" md="5">

         

      </b-col>
  </b-row>
     </Layout>

</template>

<page-query>
query {
    main: insert (path: "/content/mentorship/") {
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
        title: "GMN - Mentorship Guidelines"
    }
}
</script>