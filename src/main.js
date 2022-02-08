// This is the main.js file. Import global CSS and scripts here.
// The Client API can be used here. Learn more: gridsome.org/docs/client-api

import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import '~/assets/styles.scss'

import DefaultLayout from "~/layouts/Default.vue";


//eslint-disable-next-line no-unused-vars
export default function (Vue, { router, head, isClient }) {
    // Set default layout as a global component
    Vue.component("Layout", DefaultLayout);

    // Make BootstrapVue available throughout your project
    Vue.use(BootstrapVue);
    Vue.use(IconsPlugin)
}
