<template>
  <div class="textcard">
    <el-card class="box-card">
      <div id="tempory">
        <div v-for="blog in blogs" :key="blog.id">
          <h2>{{ blog.title }}</h2>
          <p>{{ blog.content }}</p>
          <p>发布时间:{{ blog.created }}</p>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
import {getBlog} from 'network/home'

export default {
  name: "textcard",
  data() {
    return {
      blogs: []
    };
  },
  created() {
    getBlog().then(res => {
      this.blogs = res.data.results
    })
  }
};
</script>

<style lang="css" scoped>
.text {
  font-size: 14px;
}

.item {
  padding: 18px 0;
}

.box-card {
  width: 480px;
}
</style>
