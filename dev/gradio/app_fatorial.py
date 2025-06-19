import gradio as gr
import math

def fatorial(num):
    if num < 0:
        return 'Numero negativo'
    return math.factorial(num)

iface = gr.Interface(
    fn=fatorial,
    inputs='number',
    outputs='text',
    title='Fatorial'
)

iface.launch()