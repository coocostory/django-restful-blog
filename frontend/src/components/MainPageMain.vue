<template>
  <div class="mainpagemain">
    <div v-for="blog in blogs" :key="blog.id" id="textcard"><text-card :blog="blog"></text-card></div>
  </div>
</template>

<script>
import TextCard from 'components/TextCard'
import { getBlog } from "network/home";

export default {
  name: "mainpagemain",
  created() {
    getBlog().then(res =>{
      this.blogs = res.data.results;
    })
  },
  data() {
    return {
      blogs: []
    };
  },
  components: {
      TextCard
  }
};
</script>

<style scoped>
#textcard{
  margin-bottom: 10px;
}
</style>
