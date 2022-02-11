<template>
  <Layout>

    <!-- Learn how to use images here: https://gridsome.org/docs/images -->
    
    <header class="header">
    </header>
      <body>
        <b-container class="index-container">
        <b-row>
          <b-col>
        <h1>Mentorship...for you!</h1>

        <p>An all in one program targeted to speed up your growth!</p>
        <a href="https://forms.gle/482EoBYtJozWpYCf9" class="btn" role="button" target="_blank">Apply Now</a>
            </b-col>
            <b-col>
              <img src="/images/illustration.png" alt="two people sitting in front of a computer">
          </b-col>
          </b-row>
        </b-container>
    
    <b-container class="index-container">
     <b-card-group deck>
         <b-card class="index-card"
            title="Community"
           img-src="/images/gcc2019-grouppicture.jpg"
           img-alt="Community members at Galaxy Community Conference, 2019"
           img-top
           border-radius="10px"
           >
            <b-card-text>
               Birthed from the Galaxy Community, with it at the center.
             </b-card-text>
          </b-card>
          <b-card class="index-card"
              title="Collaboration"
             img-src="/images/linkedin-sales-solutions-QgYvORVDdd8-unsplash.jpg"
             img-alt="Four hands joined together"
             img-top
             border-radius="10px"       
              >
             <b-card-text>
                  The program is founded and sustained by the pillars of collaboration.
              </b-card-text>
           </b-card>
           <b-card class="index-card"
                title="Growth"
                img-src="/images/krakenimages-Y5bvRlcCx8k-unsplash.jpg"
                img-alt="Corporate lady smiling"
                img-top
                border-radius="10px"       
                >
                <b-card-text>
                    Your growth and expectations are our focus, and your growth drives us.
                 </b-card-text>
           </b-card>
     </b-card-group>
    </b-container>
     <b-container class="index-container">
       <b-row class="index2-row">
         <b-col>
           <img src="/images/gcc2019-grouppicture.jpg" alt="image">
         </b-col>
         <b-col>
           <h3>About Galaxy Mentor Network Program</h3>
           <p>Galaxy Mentor Network (GMN) program is an initiative by the Galaxy Community to build her members in open source projects.</p> 
            <p>The GMN program is for everyone who needs guidance in an open source project, anyone who needs help learning how to contribute to open source projects, guidance in navigating and settling into the Galaxy ecosystem.</p>
            <a href="/about/">Learn More</a><span class="fas fa-arrow-circle-right"></span>           
         </b-col>
       </b-row>
     </b-container>
     
     <b-container class="index-container">
       <b-row class="p-4">
         <b-col>
           <h3>Program Highlights</h3>
           <p>This 8-week mentorship has been designed to ensure that our GMentors and GMentees have the flexibility to learn and grow together while they work towards their intended goals and expectations.</p>
         </b-col>
         <b-col>
          <b-card class="index-card">
            <b-row class="index-row">
              <b-card-text class="index-card-text">Introductory Call- setting goals and schedules</b-card-text>
            </b-row><br>
            <b-row class="index-row">
              <b-card-text class="index-card-text">Two other meetings with the Network Manager</b-card-text>
            </b-row><br>
            <b-row class="index-row">
              <b-card-text class="index-card-text">Mid-program feedback</b-card-text>
            </b-row><br>
            <b-row class="index-row">
              <b-card-text class="index-card-text">End of program feedback</b-card-text>
            </b-row>
           </b-card>    
         </b-col>
       </b-row>
     </b-container>
   </body>
     
    

  </Layout>
</template>

<script>

export default {
  metaInfo: {
    title: 'Galaxy Mentoring Network'
  }
}

</script>

<style>
.home-links a {
  margin-right: 1rem;
}
</style>


