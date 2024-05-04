<script setup>
</script>

<template>
    <div class="marquee-wrapper" style="user-select: none;">
        <div class="marquee-content" ref="marqueeContent">

            <!-- Note v-for will be used to render the images
            the extension will be checked then the appropraite 
            tag is used -->
            <!-- add video files -->
            <div class="card-testimonial">
                <article>
                <video width="auto" height="auto" controls>
                    <source src="" type="video/mp4">
                    <!-- Your browser does not support the video tag. -->
                </video>
                <h4>Title 1</h4>
                <article class="short-description">
                    <p>Description 1</p>
                </article>
                </article>
            </div>
            <!-- Pictures -->
            <div class="card-testimonial">
                <article>
                <picture>
                    <source media="(min-width: 768px)" srcset="https://randomuser.me/api/portraits/men/1.jpg">
                    <img src="https://randomuser.me/api/portraits/men/1.jpg" alt="">
                </picture>
                <h4>Title 1</h4>
                <article class="short-description">
                    <p>Description 1</p>
                </article>
                </article>
            </div>
            <!-- embed online videos -->
            <div class="card-testimonial">
                <article>
                    <iframe width="auto" height="auto" src="https://www.youtube.com/embed/dQw4w9WgXcQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                    <h4>Title</h4>
                    <article class="short-description">
                        <p>Description</p>
                    </article>
                </article>
            </div>
        </div>
    </div>
  </template>

<style scoped>
    .marquee-wrapper {
        position: relative;
        display: flex;
        align-items: center;
        justify-content: space-between;
        overflow: auto;
        scroll-behavior:auto;
        gap: 1rem;
    }
    
    .marquee-wrapper .marquee-content {
        position: relative;
        display: flex;
        align-items: center;
        justify-content: space-evenly;
        flex-shrink: 0;
        gap: 1rem;
        margin-left: 5px;
        cursor: grab;
    }

    .marquee-wrapper.marquee-content::after{
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 50%;
        height: 100%;
        background: linear-gradient(to right, rgba(255,255, 255,0), rgba(255, 255, 255, 1), 75%);

    }
    
    .marquee-wrapper .marquee-content .card-testimonial {
        max-width: 400px;
        /* background-color:#154ec1; */
        padding: 0.5rem;
        border-radius: 1rem;
        border: 1px solid #154ec1;
        /* color: #f5f5f5; */
    }
    
    .marquee-wrapper .marquee-content .card-testimonial article picture {
        position: relative;
        min-width: 200px;
    }
    
    .marquee-wrapper .marquee-content .card-testimonial article picture img {
        width: 100%;
        height: 200px;
        border-radius: 0.5rem;
        -o-object-fit: cover;
        object-fit: cover;
        -o-object-position: 50% 15%;
        object-position: 50% 15%;
    }
    
    .marquee-wrapper .marquee-content .card-testimonial article h4 {
        font-size: 20px;
        text-transform: capitalize;
        margin-block: 1rem;
    }
    
    .marquee-wrapper .marquee-content .card-testimonial article article.short-description p {
        font-family: var(--ff-heading);
        font-size: 14px;
        font-weight: 300;
        line-height: 20px;
        margin-bottom: 1.2rem;
    }
    
    @media (max-width: 1024px) {
        .marquee-wrapper {
        overflow: auto;
        }
    }
    
    .marquee-wrapper .arrow {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        font-size: 2em;
        color: #fff;
        background: rgba(0,0,0,0.5);
        padding: 0.5em;
        cursor: pointer;
    }
    
    .marquee-wrapper .arrow-left {
        left: 10px;
    }
    
    .marquee-wrapper .arrow-right {
        right: 10px;
    }
</style>
  