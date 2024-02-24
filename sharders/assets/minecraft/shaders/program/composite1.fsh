#version 330

uniform sampler2D DiffuseSampler;
uniform sampler2D DiffuseDepthSampler;
uniform sampler2D WeatherDepthSampler;

in vec2 texCoord;

out vec4 fragColor;

vec4 encode_uint(uint i) {
    uint r = (i) % 256u;
    uint g = (i >> 8u) % 256u;
    uint b = (i >> 16u) % 256u;
    uint a = (i >> 24u) % 256u;
    return vec4(float(r) / 255.0, float(g) / 255.0, float(b) / 255.0 , float(a) / 255.0);
}

uint decode_uint(vec4 ivec) {
    ivec *= 255.0;
    return uint(ivec.r) + (uint(ivec.g) << 8u) + (uint(ivec.b) << 16u) + (uint(ivec.a) << 24u);
}

vec4 encode_depth(float depth) {
    return encode_uint(floatBitsToUint(depth)); 
}

float decode_depth(vec4 depth) {
    return uintBitsToFloat(decode_uint(depth)); 
}

void main() {
    vec4 c0 = texture(DiffuseSampler, texCoord);
    float d0 = c0.a > 0.0 ? texture(DiffuseDepthSampler, texCoord).r : 1.0;
    float d1 = texture(WeatherDepthSampler, texCoord).r;

    if (d1 < d0) {
        d0 = d1;
    }

    fragColor = encode_depth(d0);
}