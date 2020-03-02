<template>
  <div class="HeaderNav">
    <el-menu
      :default-active="activeIndex2"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
    >
      <el-menu-item index="1">主页</el-menu-item>
      <el-submenu index="2">
        <template slot="title">课程</template>
        <el-menu-item index="2-1">课程1</el-menu-item>
        <el-menu-item index="2-2">课程2</el-menu-item>
        <el-menu-item index="2-3">课程3</el-menu-item>
      </el-submenu>
      <el-menu-item index="3" disabled>新功能</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: "HeaderNav",
  data() {
    return {};
  }
};
</script>

<style lang="css" scoped></style>
