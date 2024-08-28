#include <cmath>
#include <fstream>
#include <iostream>
#include <vector>

#define K_H 3
#define K_W 3
#define input_channels 64
#define output_channels 128
#define input_height 224
#define input_width 224
#define stride 2
#define padding 1

int main()
{
    std::vector<std::vector<std::vector<float>>> a(
        input_channels, std::vector<std::vector<float>>(
                            input_height, std::vector<float>(input_width)));

    std::vector<std::vector<std::vector<std::vector<float>>>> b(
        output_channels, std::vector<std::vector<std::vector<float>>>(
                             input_channels, std::vector<std::vector<float>>(
                                                 K_H, std::vector<float>(K_W))));

    int output_height = std::floor((input_height - K_H + 2 * padding) /
                                   static_cast<float>(stride)) +
                        1;

    int output_width = std::floor((input_width - K_W + 2 * padding) /
                                  static_cast<float>(stride)) +
                       1;
    std::vector<std::vector<std::vector<float>>> c(
        output_channels, std::vector<std::vector<float>>(
                             output_height, std::vector<float>(output_width)));

    for (int k = 0; k < input_channels; k++)
    {
        for (int i = 0; i < input_height; i++)
        {
            for (int j = 0; j < input_width; j++)
            {
                a[k][i][j] = i * input_width + j + 1;
            }
        }
    }

    for (int c = 0; c < output_channels; c++)
    {
        for (int k = 0; k < input_channels; k++)
        {
            for (int l = 0; l < K_H; l++)
            {
                for (int m = 0; m < K_W; m++)
                {
                    b[c][k][l][m] = k * K_H * K_W + l * K_W + m + 1;
                }
            }
        }
    }

    for (int s = 0; s < output_channels; s++)
    {
        for (int k = 0; k < input_channels; k++)
        {
            for (int i = 0; i < input_height; i = i + stride)
            {
                for (int j = 0; j < input_width; j = j + stride)
                {
                    for (int l = 0; l < K_H; l++)
                    {
                        for (int m = 0; m < K_W; m++)
                        {
                            int ll = i + l - K_H / 2;
                            int mm = j + m - K_W / 2;

                            if (ll >= 0 && ll < input_height && mm >= 0 && mm < input_width)
                            {
                                c[s][i / stride][j / stride] += a[k][ll][mm] * b[s][k][l][m];
                            }
                        }
                    }
                }
            }
        }
    }

    std::cout << "INPUT SHAPE-->" << "[" << input_channels << "," << input_height << "," << input_width << "]" << std::endl;
    std::cout << "WEIGHTS SHAPE-->" << "[" << output_channels << "," << input_channels << "," << K_H << "," << K_W << "]" << std::endl;
    std::cout << "OUTPUT SHAPE-->" << "[" << output_channels << "," << output_height << "," << output_width << "]" << std::endl;
    std::ofstream outfile("outputcpp.bin", std::ios::binary);

    for (int s = 0; s < output_channels; s++)
    {
        for (int i = 0; i < output_height; i++)
        {
            for (int j = 0; j < output_width; j++)
            {
                outfile.write(reinterpret_cast<const char *>(&c[s][i][j]),
                              sizeof(c[s][i][j]));
            }
        }
    }

    outfile.close();

    std::cout << "Convolution completed.Output data written to outputcpp.bin" << std::endl;

    return 0;
}
