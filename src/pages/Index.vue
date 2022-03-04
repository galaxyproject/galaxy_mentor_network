<template>
  <Layout>
    <b-container class="index-container">

      <b-row class="index-row">
        <b-col align-self="center">
          <h1>Mentorship... for you!</h1>
          <p>An all in one program targeted to speed up your growth!</p>
          <a href="https://forms.gle/482EoBYtJozWpYCf9" class="btn" role="button" target="_blank">Apply Now</a>
        </b-col>
        <b-col>
          <g-image src="~/images/illustration.png" alt="two people sitting in front of a computer" class="index-image"/>
        </b-col>
      </b-row>

      <b-row class="index-row">
        <b-col class="index-column">
          <g-image src="~/images/undraw_connected_world.svg" alt="image showing connected world" class="index-image index-small-image"/>
          <h3>Community</h3>
          <p>Birthed from the Galaxy Community, with it at the center.</p>
        </b-col>
        <b-col class="index-column">
          <g-image src="~/images/undraw_collaborators.svg" alt="people working together" class="index-image index-small-image"/>
          <h3>Collaboration</h3>
          <p>The program is founded and sustained by the pillars of collaboration.</p>
        </b-col>
        <b-col class="index-column">
          <g-image src="~/images/undraw_progress_data.svg" alt="progress data chart" class="index-image index-small-image"/>
          <h3>Growth</h3>
          <p>Your growth and expectations are our focus, and your growth drives us.</p>
        </b-col>
      </b-row>

      <b-row class="index-row">
        <b-col>
          <g-image src="~/images/GMN_text_poster.jpg" alt="image showing words related to mentorship" class="index-image"/>
        </b-col>
        <b-col>
          <h3>About Galaxy Mentor Network Program</h3>
          <p>Galaxy Mentor Network (GMN) program is an initiative by the Galaxy Community to build her members in open source projects.</p>
          <p>The GMN program is for everyone who needs guidance in an open source project, anyone who needs help learning how to contribute to open source projects, guidance in navigating and settling into the Galaxy ecosystem.</p>
          <p><span class="fas fa-arrow-circle-right"></span>&nbsp;<a href="/about/">Learn More</a></p>
        </b-col>
      </b-row>

      <b-row class="index-row">
        <h3>Program Highlights</h3>
        <p>This 8-week mentorship has been designed to ensure that our GMentors and GMentees have the flexibility to learn and grow together while they work towards their intended goals and expectations.</p>
        <g-image src="~/images/Program_timeline.svg" alt="Image showing program highlights" class="index-image index-image-timeline"/>
      </b-row>
      <b-row class="index-row">
        <b-col>
         <h3>Find out more about GMN</h3>
         <p><i class="fas fa-file-video"></i> Watch the presentation from our Outreachy interns (December 2021-March 2022 cohort) <a href="https://github.com/Chinonyemildred">Chinonye Mildred</a> and <a href="https://github.com/rahmot">Rahmot Afolabi</a> to know more about Galaxy Mentor Network.</p>
        </b-col>
        <b-col>
         <iframe width="560" height="315" src="https://www.youtube.com/embed/w5PbI0lJGZc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </b-col>
      </b-row>

      <!-- Testimonial carousel section. Trying to create three-cards slider containing image, and testimony-->
      <!--Caroussel doc: https://bootstrap-vue.org/docs/components/carousel -->
     <!-- <b-row class="index-row">
        <b-carousel
          id="carousel-1"
          v-model="slide"
          :interval="4000"
          controls
          indicators
          background="#ababab"
          img-width="1024"
          img-height="480"
          style="text-shadow: 1px 1px 2px #333;"
          @sliding-start="onSlideStart"
          @sliding-end="onSlideEnd"
        >-->
          <!-- Text slides with image
          <b-carousel-slide
            caption="First slide"
            text="Nulla vitae elit libero, a pharetra augue mollis interdum."
            img-src="https://picsum.photos/1024/480/?image=52"
          ></b-carousel-slide>-->

          <!-- Slides with custom text
          <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=54">
            <h1>Hello world!</h1>
          </b-carousel-slide>-->

          <!-- Slides with image only
          <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=58"></b-carousel-slide>-->

          <!-- Slides with img slot -->
          <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment
          <b-carousel-slide>
            <template #img>
              <img
                class="d-block img-fluid w-100"
                width="1024"
                height="480"
                src="https://picsum.photos/1024/480/?image=55"
                alt="image slot"
              >
            </template>
          </b-carousel-slide>-->

          <!-- Slide with blank fluid image to maintain slide aspect ratio
          <b-carousel-slide caption="Blank Image" img-blank img-alt="Blank image">
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eros felis, tincidunt
              a tincidunt eget, convallis vel est. Ut pellentesque ut lacus vel interdum.
            </p>
          </b-carousel-slide>
        </b-carousel>
      </b-row> -->
    </b-container>
  </Layout>
</template>

<script>

export default {
  metaInfo: {
    title: 'Galaxy Mentoring Network'
  },
  data() {
    return {
      slide: 0,
      sliding: null
    }
  },
  methods: {
    onSlideStart(slide) {
      this.sliding = true
    },
    onSlideEnd(slide) {
      this.sliding = false
    }
  }
}
</script>

