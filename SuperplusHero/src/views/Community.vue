<template>
    <section class="content">
        <div class="container posts-content">
            <div class="row">
                <div class="col-lg-6">
                    <div class="card mb-4">
                        <div class="card-body">
                            <div class="media mb-3">
                                <img src="https://bootdey.com/img/Content/avatar/avatar3.png"
                                    class="d-block ui-w-40 rounded-circle" alt="">
                                <div class="media-body ml-3">
                                    Kenneth Frazier
                                    <div class="text-muted small">3 days ago</div>
                                </div>
                            </div>

                            <p>
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus finibus commodo bibendum.
                                Vivamus laoreet blandit odio, vel finibus quam dictum ut.
                            </p>
                            <a href="" class="ui-rect ui-bg-cover"
                                style="background-image: url('https://bootdey.com/img/Content/avatar/avatar3.png');"></a>
                        </div>
                        <div class="card-footer">
                            <a href="#" class="d-inline-block text-muted like-button" @click="incrementCount">
                                <small class="align-middle">
                                    <strong class="like-count">{{ count + 109 }}</strong> Likes
                                </small>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
  data() {
    return {
      count: 0
    }
  },
  methods: {
    incrementCount() {
      this.count++;
    }
  }
}
</script>

<style>
.content {
    margin-top: 100px;
}

/* body {
    background:#eee;
} */

.posts-content {
    margin-top: 20px;
}

.ui-w-40 {
    width: 40px !important;
    height: auto;
}

.default-style .ui-bordered {
    border: 1px solid rgba(24, 28, 33, 0.06);
}

.ui-bg-cover {
    background-color: transparent;
    background-position: center center;
    background-size: cover;
}

.ui-rect {
    padding-top: 50% !important;
}

.ui-rect,
.ui-rect-30,
.ui-rect-60,
.ui-rect-67,
.ui-rect-75 {
    position: relative !important;
    display: block !important;
    padding-top: 100% !important;
    width: 100% !important;
}

.d-flex,
.d-inline-flex,
.media,
.media>:not(.media-body),
.jumbotron,
.card {
    -ms-flex-negative: 1;
    flex-shrink: 1;
}

.bg-dark {
    background-color: rgba(24, 28, 33, 0.9) !important;
}

.card-footer,
.card hr {
    border-color: rgba(24, 28, 33, 0.06);
}

.ui-rect-content {
    position: absolute !important;
    top: 0 !important;
    right: 0 !important;
    bottom: 0 !important;
    left: 0 !important;
}

.default-style .ui-bordered {
    border: 1px solid rgba(24, 28, 33, 0.06);
}
</style>
