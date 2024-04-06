<script lang="ts">
    export let mobileMenuIsOpened: boolean;
</script>

<section
        class={`absolute w-100 w-dvw h-dvh w-100 bg-black z-10 top-0 left-0
        translate-x-${mobileMenuIsOpened === false ? "full" : "0"} transition-transform
        flex flex-col justify-start pt-48 gap-3 text-lg
        pb-20
        `}
>
    <h2 class="text-3xl mb-12">Welcome, <strong>Robert</strong></h2>

    <span>Journeys</span>
    <span>Add new journey</span>

    <span>Settings</span>
    <span>Profile</span>

    <span class="grow"></span>

    <span class="text-red-500">Logout</span>
    <span class="mt-4">Powered by: <strong>grindset</strong></span>
</section>
