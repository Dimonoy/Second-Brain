<script lang="ts">
  import router from 'page'

  import Home from './pages/Home.svelte'

  let page
  let params

  router('/', () => page = Home)
</script>
