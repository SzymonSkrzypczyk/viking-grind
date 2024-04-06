<script lang="ts">
    import {writable} from "svelte/store";

    import Logo from '@/assets/viking_svg/LOGO.svg'
    import ShipImage from '@/assets/viking_svg/SHIP.svg'

    import Button from "@/components/Button.svelte";
    import Input from "@/components/Input.svelte";
    import MainAppNavigation from "@/components/MainAppNavigation.svelte";

    interface APIRequest {
        text: string;
        currentState: string
        step: number
    }

    const apiRequest = writable<APIRequest>({
        text: "",
        currentState: "",
        step: 0
    });

    let formCurrentStep: "text" | "currentState" | "step" = "text";

    function proceedWithForm() {
        if (formCurrentStep === "text") {
            formCurrentStep = "currentState";
        } else if (formCurrentStep === "currentState") {
            formCurrentStep = "step";
        } else {
            alert("Form is submitted")
        }
    }

    let mobileMenuIsOpened: boolean = false

</script>

<!--NAVIGATION -->

<main class="w-full flex-col justify-items-start flex gap-4">
    <MainAppNavigation mobileMenuIsOpened={mobileMenuIsOpened}/>

    <header class="w-full flex items-center gap-8 relative z-20">
        <div class="relative aspect-square w-16">
            <img src={Logo} alt="logo" class="absolute scale-150"/>
        </div>

        <h2 class="text-3xl flex-grow text-left">Natka.io</h2>

        <button on:click={()=>mobileMenuIsOpened= !mobileMenuIsOpened}>
            {#if mobileMenuIsOpened}
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                     xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                          d="M6 18L18 6M6 6l12 12"></path>
                </svg>
            {:else}
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                     xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                          d="M4 6h16M4 12h16m-7 6h7"></path>
                </svg>
            {/if}
        </button>
    </header>

    <section class="flex-grow w-full flex flex-col justify-center p-6">
        <div class="w-full h-80 mb-4 relative">
            <img src={ShipImage} alt="ship" class="absolute"/>
        </div>

        <h1 class="text-7xl font-bold">Embark</h1>
        <h2 class="text-2xl opacity-80">on a new journey</h2>

        <p class="my-4 text-lg opacity-80">What do you want to achieve?</p>

        <Input placeholder="Describe your dreams..."
               classes="mt-5 mb-2"
               bind:value={$apiRequest.text}
        />

        <Button variant="indigo"
                label={formCurrentStep === "step" ? "Submit" : "Continue"}
                disabled={$apiRequest.text.length < 10}
                on:click={proceedWithForm}
        />

        <span class="flex-grow"></span>

        <span>Powered by: <strong>grindset</strong></span>
    </section>
</main>

<style lang="sass">
  main
    height: 98vh

</style>