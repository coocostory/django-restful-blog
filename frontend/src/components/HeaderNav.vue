<template>
  <div class="HeaderNav">
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
      :router="true"
    >
      <el-menu-item index="/">主页</el-menu-item>
      <el-menu-item index="/course">课程</el-menu-item>
      
      <el-menu-item index="/new" disabled>新功能</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: "HeaderNav",
  data() {
    return {
      activeIndex: "/"
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
      this.activeIndex = key;
    }
  }
};
</script>

<style lang="css" scoped></style>
