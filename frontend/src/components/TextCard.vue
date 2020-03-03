<template>
  <div class="textcard">
    <el-card class="box-card">
      <div id="title">{{ blog.title }}</div>
      <div id="context">{{ blog.content }}</div>
      <div id="pubdate">发布时间:{{ pubdate }}</div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "textcard",
  props: {
    blog: {
      type: Array,
      default() {
        return [];
      }
    }
  },
  data() {
    return {
      pubdate:
        this.blog.created.substring(0, 10) +
        " " +
        this.blog.created.substring(11, 19)
    };
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
  width: 880px;
}

#title {
  margin: -7px 0 4px;
  display: inherit;
  font-size: 18px;
  font-weight: 700;
  line-height: 1.5;
}
#pubdate {
  font-size: 12px;
  font-weight: 400;
  line-height: 20px;
  color: #787878
}
</style>
