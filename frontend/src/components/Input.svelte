<script lang="ts">
    import {createEventDispatcher} from "svelte";

    const dispatch = createEventDispatcher();
    export let value: string;
    export let placeholder: string

    export let classes: string = ""

    function onKeydownHandler({key}: KeyboardEvent) {
        if (key === "Enter") {
            dispatch("pressingEnter", "prop")
        }
    }

</script>

<input
        value={value}
        placeholder={placeholder}
        on:input={(e)=>value = e.currentTarget.value}
        on:keydown={onKeydownHandler}

        class={`py-2 px-4 border-stone-100 border-2 rounded-md w-full focus:outline-none focus:border-indigo-500 transition duration-300 ease-in-out ${classes}`}
/>