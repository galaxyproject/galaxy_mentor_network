<template>
     <Layout>
         <b-row>
      <b-col lg="7" md="7">
            <h1 class="page-title">{{ $page.main.title }}</h1>
            <div class="markdown" v-html="$page.main.content" /> 
         </b-col>
      <b-col lg="5" md="5">

          <h2>Mentorship Training</h2>
          <p>We encourage all participants to watch this video on open source mentorship.</p>
          <iframe width="100%" height="314" src="https://www.youtube.com/embed/6W5najMfcy0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
          <p>Video credit: MongoDB</p>
          <p>More information to guide you can be found in this <a href="https://www.mentorship.guide/" target="_blank">resource</a></p>

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