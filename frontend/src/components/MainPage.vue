<template>
  <div class="MainPage">
    <el-container id="mypage">
      <el-header><header-nav></header-nav></el-header>
      <el-main><router-view></router-view></el-main>
      <el-footer><foot-nav></foot-nav></el-footer>
    </el-container>
  </div>
</template>

<script>
import HeaderNav from "components/HeaderNav";
import FootNav from "components/FootNav";

export default {
  name: "MainPage",
  components: {
    HeaderNav,
    FootNav
  },
  data() {
    return {};
  }
};
</script>

<style lang="css" scoped>
#mypage {
  padding: 0px
}
</style>
