<script setup lang="ts">
import MainPanelVue from './components/MainPanel.vue'
import Controller from './components/Controller.vue'
import { ref } from 'vue'

const abc = ref(1)

</script>

<template>
<div class="container">
  <MainPanelVue></MainPanelVue>
  <Controller value-name="abc" v-model="abc" :range="[1,10]" :is-integer="true"></Controller>
</div>
</template>

<style>
</style>
