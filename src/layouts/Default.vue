<template>
    <div class="layout">
        <header class="masthead">
            <b-navbar class="container justify-content-center" toggleable="lg">
                <b-navbar-brand href="#">
                    <img src="src/favicon.png" class="d-inline-block align-top" alt="GMN Logo">
                  {{ $static.metadata.siteName }}
                </b-navbar-brand>
                <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
                <b-collapse id="nav-collapse" is-nav>
                    <b-navbar-nav id="navbar-menu">
                        <b-nav-item href="/about/">About</b-nav-item>
                        <b-nav-item-dropdown text="Guides" right>
                            <b-dropdown-item href="#">Application Guidelines</b-dropdown-item>
                            <b-dropdown-item href="#">Mentorship Guidelines</b-dropdown-item>
                        </b-nav-item-dropdown>
                        <b-nav-item href="/faq/">FAQ</b-nav-item>
                        <b-nav-item disabled>Project & Participants</b-nav-item>
                        <b-nav-item href="/blog/">Blog</b-nav-item>
                    </b-navbar-nav>
                </b-collapse>
            </b-navbar>
        </header>
        <main id="maincontainer" class="container">
            <slot />
        </main>
        <footer class="static-footer"/>
    </div>
</template>

<static-query>
query {
  metadata {
    siteName
  }
}
</static-query>

