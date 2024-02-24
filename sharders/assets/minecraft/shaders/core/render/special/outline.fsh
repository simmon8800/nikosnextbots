#version 330
#define FSH

uniform sampler2D Sampler0;

uniform vec4 ColorModulator;

in vec4 vertexColor;
in vec2 texCoord0;
in vec4 glpos;

out vec4 fragColor;

void main() {
    vec4 color = texture(Sampler0, texCoord0);
    if (color.a == 0.0) discard;
    fragColor = vec4(ColorModulator.rgb * vertexColor.rgb, ColorModulator.a);
}