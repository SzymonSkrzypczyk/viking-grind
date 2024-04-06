<script lang="ts">
    import {createEventDispatcher} from 'svelte'
    import {TailwindPalette} from "@/types/tailwind";

    import type {TailwindColor} from "@/types/tailwind";

    const dispatch = createEventDispatcher();

    export let disabled: boolean = false;
    export let label: string;
    export let variant: TailwindColor = 'gray';

</script>

<button
        on:click={() => dispatch('click')}
        disabled={disabled}
        class="px-3 py-2 rounded transition duration-300 ease-in-out disabled:bg-stone-300 disabled:text-white {TailwindPalette.getColors(variant)}">
    {label}
    <slot></slot>
</button>